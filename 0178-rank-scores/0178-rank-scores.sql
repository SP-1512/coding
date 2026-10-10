select score, dense_rank() over(order by score DESC) as Rank
from scores
order by Rank;