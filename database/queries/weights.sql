-- name: ListWeights :many
SELECT *
FROM weights
ORDER BY id;

-- name: CreateWeights :exec
INSERT INTO weights (from_node_id, to_node_id, distance)
VALUES ($1, $2, $3);

