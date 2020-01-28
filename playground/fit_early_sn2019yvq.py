from fit_just_early_lc import fit_lc
import pandas as pd

prep_df = pd.read_hdf('/projects/p30796/ZTF/SN2019yvq/first_light_4d_2019yvq.h5')
t_data = prep_df.t_data.values
f_data = prep_df.f_data.values
f_unc_data = prep_df.f_unc_data.values
fcqfid_data = prep_df.fcqfid_data.values

fit_lc(t_data, f_data, f_unc_data, fcqfid_data,
       mcmc_h5_file='/projects/p30796/ZTF/SN2019yvq/sn2019yvq_4d_emcee.h5', 
       max_samples=10000, 
       ncores=5,
       use_emcee_backend=True,
       thin_by=100,
       rel_flux_cutoff=0.4,
       prior='uninformative'
       )