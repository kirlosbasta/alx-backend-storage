--  lists all bands with Glam rock as their main style, ranked by their longevity
SELECT band_name, CASE WHEN split IS NOT NULL THEN split - formed ELSE YEAR(CURDATE()) - formed END AS lifespan FROM metal_bands WHERE style LIKE "%Glam rock%" ORDER BY lifespan DESC;
