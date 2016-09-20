from astroquery.sdss import SDSS


QUERY = """
SELECT TOP {N}
p.psfMag_r, p.fiberMag_r, p.fiber2Mag_r, p.petroMag_r, 
p.deVMag_r, p.expMag_r, p.modelMag_r, p.cModelMag_r, 
s.class
FROM PhotoObjAll AS p JOIN specObjAll s ON s.bestobjid = p.objid
WHERE p.mode = 1 AND s.sciencePrimary = 1 AND p.clean = 1 AND s.class != 'QSO'
ORDER BY p.objid ASC
"""


def get_star_galaxy_data(N=10000):
    query = QUERY.format(N=N)
    data = SDSS.query_sql(query)
    return data.to_pandas()



