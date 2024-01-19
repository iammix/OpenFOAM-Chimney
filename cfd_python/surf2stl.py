import numpy as np

def surf2stl(filename, x, y, z, mode='binary'):
    if not isinstance(filename, str):
        raise ValueError('Invalid filename')

    if mode != 'ascii':
        mode = 'binary'

    if z.ndim != 2:
        raise ValueError('Variable z must be a 2-dimensional array')

    if ((x.shape != z.shape) | (y.shape != z.shape)):
        if len(x) == 1 and len(y) == 1:
            dx, dy = x, y
            x = (np.arange(z.shape[1]) - 1) * dx
            y = (np.arange(z.shape[0]) - 1) * dy
        elif (len(x) == z.shape[1]) and (len(y) == z.shape[0]):
            xvec, yvec = x, y
            x, y = np.meshgrid(xvec, yvec)
        else:
            raise ValueError('Unable to resolve x and y variables')

    with open(filename, 'wb+') as fid:
        title_str = f'Created by surf2stl.py {np.datetime64("now")}'
        
        if mode == 'ascii':
            fid.write(f'solid {title_str}\r\n'.encode())
        else:
            fid.write(title_str.ljust(80).encode())  # Title
            fid.write(np.int32(0).tobytes())  # Number of facets, zero for now

        nfacets = 0

        for i in range(z.shape[0] - 2):
            for j in range(z.shape[1] - 1):
                p1 = [x[i, j], y[i, j], z[i, j]]
                p2 = [x[i, j + 1], y[i, j + 1], z[i, j + 1]]
                p3 = [x[i + 1, j + 1], y[i + 1, j + 1], z[i + 1, j + 1]]
                val = local_write_facet(fid, p1, p2, p3, mode)
                nfacets += val

                p1 = [x[i + 1, j + 1], y[i + 1, j + 1], z[i + 1, j + 1]]
                p2 = [x[i + 1, j], y[i + 1, j], z[i + 1, j]]
                p3 = [x[i, j], y[i, j], z[i, j]]
                val = local_write_facet(fid, p1, p2, p3, mode)
                nfacets += val

        last_row = z.shape[0] - 2
        for j in range(z.shape[1]-1):
            p1 = [x[last_row, j], y[last_row, j], z[last_row, j]]
            p2 = [x[last_row, j + 1], y[last_row, j + 1], z[last_row, j + 1]]
            p3 = [x[last_row + 1, j + 1], y[last_row + 1, j + 1], z[last_row + 1, j + 1]]
            val = local_write_facet(fid, p1, p2, p3, mode)
            nfacets += val

        if mode == 'ascii':
            fid.write(f'endsolid {title_str}\r\n'.encode())
        else:
            fid.seek(0, 0)
            fid.seek(80, 0)
            fid.write(np.int32(nfacets).tobytes())

    print(f'Wrote {nfacets} facets')


def local_write_facet(fid, p1, p2, p3, mode):
    if np.isnan(p1).any() or np.isnan(p2).any() or np.isnan(p3).any():
        return 0
    else:
        n = local_find_normal(p1, p2, p3)
        num = 1

        if mode == 'ascii':
            fid.write(f'facet normal {n[0]:.7E} {n[1]:.7E} {n[2]:.7E}\r\n'.encode())
            fid.write(b'outer loop\r\n')
            fid.write(f'vertex {p1[0]:.7E} {p1[1]:.7E} {p1[2]:.7E}\r\n'.encode())
            fid.write(f'vertex {p2[0]:.7E} {p2[1]:.7E} {p2[2]:.7E}\r\n'.encode())
            fid.write(f'vertex {p3[0]:.7E} {p3[1]:.7E} {p3[2]:.7E}\r\n'.encode())
            fid.write(b'endloop\r\n')
            fid.write(b'endfacet\r\n')
        else:
            fid.write(np.float32(n).tobytes())
            fid.write(np.float32(p1).tobytes())
            fid.write(np.float32(p2).tobytes())
            fid.write(np.float32(p3).tobytes())
            fid.write(np.int16(0).tobytes())  # unused

    return num


def local_find_normal(p1, p2, p3):
    v1 = np.array(p2) - np.array(p1)
    v2 = np.array(p3) - np.array(p1)
    v3 = np.cross(v1, v2)
    n = v3 / np.sqrt(np.sum(v3 * v3))
    return n
