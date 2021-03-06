import subprocess

def showState(cell_log):
    cell_log.collect('GitHub State')
    cell_log.collect('============')
    cell_log.collect('* Branch: {}'.format(getBranch()))
    cell_log.collect('* Branches: {}'.format(getBranchList()))
    cell_log.collect('* Contributors: {}'.format(getContributorList()))
    
def getBranch():
    '''
    return current branch name
    '''
    rc = subprocess.check_output(["git", "branch", "--contains", "HEAD"]).decode().replace('* ','')
    return rc
    
def getBranchList():
    '''
    return list of user assigned to repo
    
    '''
    bytelist = subprocess.check_output(["git", "branch"])
    _list = bytelist.decode().split() 
    return _list

def getContributorList():
    '''
    %an author name
    %aN 
    return list of contributors for this repo
    '''
    
    cmd = 'git log --pretty="%aN %ae%n%cn %ce" | sort | uniq'
    cmd = 'git log --pretty="%ae%n%cn %ce" | sort | uniq'
    cmd = 'git log --pretty="%ce" | sort | uniq'
    ps = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    bytelist = ps.communicate()[0]
    
    _list = bytelist.decode().split() 
    return _list

print("branch: "+ getBranch())
print("branches: ", getBranchList())
print("users: ", getContributorList())

