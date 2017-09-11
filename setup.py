import git
import os


local_path_root = 'C:\\Users\\kshit\\Dropbox\\workspace\\tic\\tic\\'
repo_url_root = 'https://github.com/theimagingcollective'
repos = ['read_dicom', 'slice_timing']
extension = '.git'

for repo_ in repos:
	target_dir = os.path.join(local_path_root, repo_)
	repo_url = ''.join([repo_url_root, '/', repo_, extension])
	try:
		git.Repo.clone_from(repo_url, target_dir)
	except git.exc.GitCommandError as excep:
		print(excep.stderr)





