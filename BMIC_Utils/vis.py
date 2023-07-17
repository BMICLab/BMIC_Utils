import pandas as pd
import numpy as np
from types import Tuple


def get_mri_indices(mri) -> Tuple[int, int, int]:
    """get (x,y,z) indices of best channels to visualize given MRI image

    :param mri: 3D MRI scan
    :return:
    """
    nz_indices = mri.nonzero()
    df = pd.DataFrame(np.array(nz_indices).T, columns=['x', 'y', 'z'])
    x_dy = df.groupby('x')['y'].agg(np.ptp)
    x_idx = int(x_dy.idxmax())

    y_dz = df.groupby('y')['z'].agg(np.ptp)
    y_idx = int(y_dz.idxmax())

    z_dx = df.groupby('z')['x'].agg(np.ptp)
    z_idx = int(z_dx.idxmax())
    return x_idx, y_idx, z_idx