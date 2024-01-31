-- name: ListNodes :many
SELECT *
FROM nodes
ORDER BY id;

-- name: CreateNode :exec
INSERT INTO nodes (name, point_geom)
VALUES ($1, $2);

