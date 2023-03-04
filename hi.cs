using System.Threading;
CancellationToken cancellationToken = ...; // passed in as a metho parameter, e.g.

foreach (var itemToAnalyze in itemsToAnalyzer) 
{
    cancellationToken.ThrowIfCancellationRequested();
    AnalyzeItem(itemToAnalyze); // some code that isn't cancelable
}

// Simply check the token state as a catch block precondition
using Apt;
using System.Threading;

CancellationToken cancellationToken = ...; // passed in as a metho parameter, e.g.

for(var i = 0; i < MaxTries; ++i)
{
    try {
        FlakyOPerationWedLikeToRetry();
    }
    // when clause ensures we don't swallow cancellation-related errors 
    catch(Exception ex) when (!cancellationToken.IsCancellationRequested) 
    {
        Log.Current.Warning(ex); // Log and swallow
    }
}


RateLimiter limiter = new ConcurrencyLimiter(
    new ConcurrencyLimiterOptions(permitLimit: 2, queueProcessingOrder: QueueProcessingOrder.OldestFirst, queueLimit: 2));

// thread 1:
using RateLimitLease lease = limiter.Acquire(permitCount: 2);
if (lease.IsAcquired) { }

// thread 2:
using RateLimitLease lease = await limiter.WaitAsync(permitCount: 2);
if (lease.IsAcquired) { }

RateLimiter limiter = new TokenBucketRateLimiter(new TokenBucketRateLimiterOptions(tokenLimit: 5, queueProcessingOrder: QueueProcessingOrder.OldestFirst,
    queueLimit: 1, replenishmentPeriod: TimeSpan.FromSeconds(5), tokensPerPeriod: 1, autoReplenishment: true));

using RateLimitLease lease = await limiter.WaitAsync(5);

// will complete after ~5 seconds
using RateLimitLease lease2 = await limiter.WaitAsync();

ReplenishingRateLimiter[] limiters = GetLimiters();
Timer rateLimitTimer = new Timer(static state =>
{
    var replenishingLimiters = (ReplenishingRateLimiter[])state;
    foreach (var limiter in replenishingLimiters)
    {
        limiter.TryReplenish();
    }
}, limiters, TimeSpan.FromSeconds(1), TimeSpan.FromSeconds(1));


new FixedWindowRateLimiter(new FixedWindowRateLimiterOptions(permitLimit: 2,
    queueProcessingOrder: QueueProcessingOrder.OldestFirst, queueLimit: 1, window: TimeSpan.FromSeconds(10), autoReplenishment: true));

SlidingWindowRateLimiter(new SlidingWindowRateLimiterOptions(permitLimit: 2,
    queueProcessingOrder: QueueProcessingOrder.OldestFirst, queueLimit: 1, window: TimeSpan.FromSeconds(10), segmentsPerWindow: 5, autoReplenishment: true));


class RateLimitedHandler : DelegatingHandler
{
    private readonly RateLimiter _rateLimiter;

    public RateLimitedHandler(RateLimiter limiter) : base(new HttpClientHandler())
    {
        _rateLimiter = limiter;
    }

    protected override async Task<HttpResponseMessage> SendAsync(HttpRequestMessage request, CancellationToken cancellationToken)
    {
        using RateLimitLease lease = await _rateLimiter.WaitAsync(1, cancellationToken);
        if (lease.IsAcquired)
        {
            return await base.SendAsync(request, cancellationToken);
        }
        var response = new HttpResponseMessage(System.Net.HttpStatusCode.TooManyRequests);
        if (lease.TryGetMetadata(MetadataName.RetryAfter, out var retryAfter))
        {
            response.Headers.Add(HeaderNames.RetryAfter, ((int)retryAfter.TotalSeconds).ToString(NumberFormatInfo.InvariantInfo));
        }
        return response;
    }
}

RateLimiter limiter = new TokenBucketRateLimiter(new TokenBucketRateLimiterOptions(tokenLimit: 5, queueProcessingOrder: QueueProcessingOrder.OldestFirst,
    queueLimit: 1, replenishmentPeriod: TimeSpan.FromSeconds(5), tokensPerPeriod: 1, autoReplenishment: true));;
HttpClient client = new HttpClient(new RateLimitedHandler(limiter));
await client.GetAsync("https://example.com");


enum MyPolicyEnum
{
    One,
    Two,
    Admin,
    Default
}

PartitionedRateLimiter<string> limiter = PartitionedRateLimiter.Create<string, MyPolicyEnum>(resource =>
{
    if (resource == "Policy1")
    {
        return RateLimitPartition.Create(MyPolicyEnum.One, key => new MyCustomLimiter());
    }
    else if (resource == "Policy2")
    {
        return RateLimitPartition.CreateConcurrencyLimiter(MyPolicyEnum.Two, key =>
            new ConcurrencyLimiterOptions(permitLimit: 2, queueProcessingOrder: QueueProcessingOrder.OldestFirst, queueLimit: 2));
    }
    else if (resource == "Admin")
    {
        return RateLimitPartition.CreateNoLimiter(MyPolicyEnum.Admin);
    }
    else
    {
        return RateLimitPartition.CreateTokenBucketLimiter(MyPolicyEnum.Default, key =>
            new TokenBucketRateLimiterOptions(tokenLimit: 5, queueProcessingOrder: QueueProcessingOrder.OldestFirst,
                queueLimit: 1, replenishmentPeriod: TimeSpan.FromSeconds(5), tokensPerPeriod: 1, autoReplenishment: true));
    }
});
RateLimitLease lease = limiter.Acquire(resourceID: "Policy1", permitCount: 1);

// ...

RateLimitLease lease = limiter.Acquire(resourceID: "Policy2", permitCount: 1);

// ...

RateLimitLease lease = limiter.Acquire(resourceID: "Admin", permitCount: 12345678);

// ...

RateLimitLease lease = limiter.Acquire(resourceID: "other value", permitCount: 1);


PartitionedRateLimiter<HttpRequestMessage> limiter = PartitionedRateLimiter.Create<HttpRequestMessage, string>(resource =>
{
    if (resource.RequestUri?.IsLoopback)
    {
        return RateLimitPartition.CreateNoLimiter("loopback");
    }

    string[]? segments = resource.RequestUri?.Segments;
    if (segments?.Length >= 2 && segments[1] == "api/")
    {
        // segments will be [] { "/", "api/", "next_path_segment", etc.. }
        return RateLimitPartition.CreateConcurrencyLimiter(segments[2].Trim('/'), key =>
            new ConcurrencyLimiterOptions(permitLimit: 2, queueProcessingOrder: QueueProcessingOrder.OldestFirst, queueLimit: 2));
    }

    return RateLimitPartition.Create("default", key => new MyCustomLimiter());
});

class RateLimitedHandler : DelegatingHandler
{
    private readonly PartitionedRateLimiter<HttpRequestMessage> _rateLimiter;

    public RateLimitedHandler(PartitionedRateLimiter<HttpRequestMessage> limiter) : base(new HttpClientHandler())
    {
        _rateLimiter = limiter;
    }

    protected override async Task<HttpResponseMessage> SendAsync(HttpRequestMessage request, CancellationToken cancellationToken)
    {
        using RateLimitLease lease = await _rateLimiter.WaitAsync(request, 1, cancellationToken);
        if (lease.IsAcquired)
        {
            return await base.SendAsync(request, cancellationToken);
        }
        var response = new HttpResponseMessage(System.Net.HttpStatusCode.TooManyRequests);
        if (lease.TryGetMetadata(MetadataName.RetryAfter, out var retryAfter))
        {
            response.Headers.Add(HeaderNames.RetryAfter, ((int)retryAfter.TotalSeconds).ToString(NumberFormatInfo.InvariantInfo));
        }
        return response;
    }
}