from DE import *
import scipy.constants as sc

# IV-FSTT  DOUBLE DIODE #######################

b = {'rp':  [2, 100],
     'rs':  [0, 1],
     'a1':   [1, 2],
     'a2':   [1, 2],
     'i01':  [1e-07, 1e-04],
     'i02':  [1e-07, 1e-04],
     'ipv': [0, 10]
     }

T = 33 + 275.15
algo = DE(b, [*read_csv("data/IV-FSTT.csv")], 1, 1, T)
algo.solve()
algo.plot_fit_hist()
algo.plot_result(print_params=True)

# poly-670w  DOUBLE DIODE #######################
# b = {'rp':  [2, 100],
#      'rs':  [0, 1],
#      'a1':   [1, 2],
#      'a2':   [1, 2],
#      'i01':  [1e-07, 1e-04],
#      'i02':  [1e-07, 1e-04],
#      'ipv': [0, 10]
#      }
#
# T = 33 + 275.15
# algo = DE(b, [*read_csv("data/poly-670w.csv")], 1, 1, T)
# algo.solve()
# algo.plot_fit_hist()
# algo.plot_result(print_params=True)

# poly2-1300w DOUBLE DIODE #######################

# b = {'rp':  [2, 100],
#      'rs':  [0, 1],
#      'a1':   [1, 2],
#      'a2':   [1, 2],
#      'i01':  [1e-07, 1e-04],
#      'i02':  [1e-07, 1e-04],
#      'ipv': [0, 10]
#      }

# T = 33 + 275.15
# algo = DE(b, [*read_csv("data/poly2-1300w.csv")], 1, 1, T)
# algo.solve()
# algo.plot_fit_hist()
# algo.plot_result(print_params=True)

# cellul-mono DOUBLE DIODE #######################

# b = {'rp':  [2, 100],
#      'rs':  [0, 1],
#      'a1':   [1, 2],
#      'a2':   [1, 2],
#      'i01':  [1e-07, 1e-04],
#      'i02':  [1e-07, 1e-04],
#      'ipv': [0, 10]
#      }

# T = 33 + 275.15
# algo = DE(b, [*read_csv("data/cellul-mono.csv")], 1, 1, T)
# algo.solve()
# algo.plot_fit_hist()
# algo.plot_result(print_params=True)

