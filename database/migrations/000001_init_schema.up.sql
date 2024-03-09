CREATE
    EXTENSION IF NOT EXISTS postgis;

-- Create the 'node' table
CREATE TABLE "node" (
                        "id" BIGSERIAL PRIMARY KEY,
                        "name" VARCHAR NOT NULL UNIQUE,
                        "geom" GEOMETRY(POINT, 3857) NOT NULL UNIQUE
);

-- Create the 'edge' table
CREATE TABLE "edge" (
                        "id" BIGSERIAL PRIMARY KEY,
                        "from_node_id" BIGINT NOT NULL,
                        "to_node_id" BIGINT NOT NULL,
                        "weight" DOUBLE PRECISION NOT NULL,
                        CONSTRAINT "fk_from_node_id" FOREIGN KEY ("from_node_id") REFERENCES "node" ("id"),
                        CONSTRAINT "fk_to_node_id" FOREIGN KEY ("to_node_id") REFERENCES "node" ("id"),
                        CONSTRAINT "edge_unique_constraint" UNIQUE ("from_node_id", "to_node_id")
);

-- Create the 'place' table
CREATE TABLE "place" (
                         "id" BIGSERIAL PRIMARY KEY,
                         "name" VARCHAR NOT NULL,
                         "location" GEOMETRY(POINT, 3857)
);

-- Create the 'building' table
CREATE TABLE "building" (
                            "id" BIGSERIAL PRIMARY KEY,
                            "name" VARCHAR NOT NULL,
                            "geom" GEOMETRY(POLYGON, 3857)
);

-- Create the 'classroom' table
CREATE TABLE "classroom" (
                             "id" BIGSERIAL PRIMARY KEY,
                             "building_id" BIGINT NOT NULL,
                             "room_code" VARCHAR NOT NULL,
                             CONSTRAINT "fk_building_id" FOREIGN KEY ("building_id") REFERENCES "building" ("id"),
                             CONSTRAINT "classroom_unique_constraint" UNIQUE ("building_id", "room_code")
);

-- Create indexes for the 'node' table
CREATE INDEX "idx_node_geom" ON "node" ("geom");

-- Create indexes for the 'edge' table
CREATE INDEX "idx_edge_from_to" ON "edge" ("from_node_id", "to_node_id");
CREATE INDEX "idx_edge_weight" ON "edge" ("weight");

-- Create indexes for the 'place' table
CREATE INDEX "idx_place_name" ON "place" ("name");
CREATE INDEX "idx_place_location" ON "place" ("location");

-- Create indexes for the 'building' table
CREATE INDEX "idx_building_name" ON "building" ("name");
CREATE INDEX "idx_building_geom" ON "building" ("geom");

-- Create indexes for the 'classroom' table
CREATE INDEX "idx_classroom_building_id" ON "classroom" ("building_id");
CREATE INDEX "idx_classroom_room_code" ON "classroom" ("room_code");
