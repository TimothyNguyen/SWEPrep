select metricItemId, metricName
from one.vmetrics
where metricName = 'Sales';

select Count(*)
from one.vmetrics
where frontSymbol = '$';

select entityName, entityId
from one.entities
where entityid = 4;

select entityId, entityName
from one.entities
where instanceIdColumn <> 'invalid'
order by entityId;

select frequencyid, frequency
from one.frequencies
where frequencyId = 2;

select d.metricName, b.entityName, c.frequency
from one.vmefs a
join one.entities b
    on a.entityId = b.entityId
join one.frequencies c
    on a.frequencyId = c.frequencyId
join one.vmetrics d
    on a.metricItemId = d.metricItemId
where d.metricName = 'Sales'
order by 1, 2, 3;