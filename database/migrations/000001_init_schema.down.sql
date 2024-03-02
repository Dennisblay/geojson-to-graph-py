-- Remove Foreign Keys
ALTER TABLE "weights"
    DROP CONSTRAINT IF EXISTS weights_to_node_id_fkey;

ALTER TABLE "weights"
    DROP CONSTRAINT IF EXISTS weights_from_node_id_fkey;

ALTER TABLE "edges"
    DROP CONSTRAINT IF EXISTS edges_node_id_fkey;

-- Drop indexes
DROP INDEX IF EXISTS ix_weights_to_node_id;
DROP INDEX IF EXISTS ix_weights_from_node_id;
DROP INDEX IF EXISTS ix_edges_node_id;
DROP INDEX IF EXISTS ix_nodes_point_geom;
DROP INDEX IF EXISTS ix_nodes_id;

-- Drop tables
DROP TABLE IF EXISTS "weights";
DROP TABLE IF EXISTS "edges";
DROP TABLE IF EXISTS "nodes";
