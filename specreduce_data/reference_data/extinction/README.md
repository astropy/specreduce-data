# Atmospheric Extinction files

Atmospheric extinction data for several observatories are collected here and described below. In each
case there are two columns: wavelength in Angstroms and extinction in mag/airmass.

|    File               |   Lon      |    Lat     |   Elevation (m) | Ref |
| --------------------- | ----------:| ----------:|----------------:|----:|
| `ctioextinct.dat`     | 70.8150    | -30.1653   |      2215.0     |  1  |
| `kpnoextinct.dat`     | 111.600    |  31.9633   |       2120.0    |  2  |
| `lapalmaextinct.dat`  | 17.8947    | 28.7636    |      2396.0     |  3  |
| `mkoextinct.dat`      | 155.47833  |  19.82833  |      4160.0     |  4  |
| `mthamextinct.dat`    | 121.6428   |  37.34139  |      1290.0     |  5  |
| `paranalextinct.dat`  | 70.4048305 | -24.627167 |       2635.4    |  6  |
| `apoextinct.dat`      | 105.82028  | 32.78028   |       2788.0    |  7  |

1. `ctioextinct.dat`: CTIO extinction table for IRAF ONEDSPEC (in Angstroms)
The CTIO extinction curve distributed with IRAF comes from the work of
Stone & Baldwin (1983 MN 204, 347) and Baldwin & Stone (1984 MN 206,
241).  The first of these papers lists the points from 3200-8370A while
the second extended the flux calibration from 6056 to 10870A but the
derived extinction curve was not given in the paper.  The IRAF table
follows SB83 out to 6436, the redder points presumably come from BS84
with averages used in the overlap region. More recent CTIO extinction
curves are shown as Figures in Hamuy et al (92, PASP 104, 533 ; 94 PASP
106, 566). -- Steve Heathcote, Mon, 19 Jul 1999

2. `kpnoextinct.dat`: KPNO extinction table for IRAF ONEDSPEC (in Angstroms)

3. `lapalmaextinct.dat`: Extinction table for Roque de Los Muchachos Observatory, La Palma.
Described in https://www.ing.iac.es/Astronomy/observing/manuals/ps/tech_notes/tn031.pdf.

4. `mkoextinct.dat`: Median atmospheric extinction data for Mauna Kea Observatory measured by the Nearby SuperNova Factory: https://www.aanda.org/articles/aa/pdf/2013/01/aa19834-12.pdf.

5. `mthamextinct.dat`: Median atmospheric extinction table for Lick Observatory on Mt. Hamilton constructed from https://mthamilton.ucolick.org/techdocs/standards/lick_mean_extinct.html.

6. `paranalextinct.dat`: Updated extinction table for ESO-Paranal taken from https://www.aanda.org/articles/aa/pdf/2011/03/aa15537-10.pdf.

7. `apoextinct.dat`: Extinction table for Apache Point Observatory. Based on the extinction table used for SDSS and
available at https://www.apo.nmsu.edu/arc35m/Instruments/DIS/ (https://www.apo.nmsu.edu/arc35m/Instruments/DIS/images/apoextinct.dat).


An additional file, `atm_trans_am1.0.dat`, is included that provides atmospheric transmission in the IR from 0.9 to 5.6 microns. The two columns are wavelength in microns and transmission at an airmass of 1. The transmission values are generated from the ATRAN model, https://atran.arc.nasa.gov/cgi-bin/atran/atran.cgi (Lord, S. D., 1992, NASA Technical Memorandum 103957).
