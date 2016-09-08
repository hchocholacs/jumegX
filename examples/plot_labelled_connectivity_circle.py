#!/usr/bin/env python

import numpy as np
from jumeg.connectivity import plot_labelled_group_connectivity_circle
from jumeg import get_jumeg_path

# load the yaml grouping of Freesurfer labels
yaml_fname = get_jumeg_path() + '/examples/rsn_aparc_cortex_grouping.yaml'

# make a random connectivity matrix with 68 nodes
con = np.random.random((68, 68))

# plotting within a subplot
plot_labelled_group_connectivity_circle(yaml_fname, con, out_fname='rsn_circle.png',
                                        show=True, n_lines=20, fontsize_names=6,
                                        title='test RSN circ labels')
