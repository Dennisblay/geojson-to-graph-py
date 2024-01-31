-- name: ListEdges :many
SELECT *
FROM edges
ORDER BY id;

-- name: CreateEdges :exec
INSERT INTO edges (node_id, edges)
VALUES ($1, $2);

