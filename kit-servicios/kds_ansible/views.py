from django.shortcuts import render
from collections import namedtuple
from ansible.playbook import Playbook
from ansible.parsing.dataloader import DataLoader
from ansible.vars import VariableManager
from ansible.inventory import Inventory
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.utils.vars import load_extra_vars
from ansible.executor.task_queue_manager import TaskQueueManager
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROLESDIR = BASE_DIR + '/recetas/ansible-role-mailserver/site.yml'

def deploy_service(username, passwd, hosts, extras):

	variable_manager = VariableManager()
	loader = DataLoader()

	inventory = Inventory(loader=loader, variable_manager=variable_manager,  host_list='/etc/ansible/hosts')
	playbook_path = ROLESDIR

	if not os.path.exists(playbook_path):
	    print '[INFO] The playbook does not exist'
	    sys.exit()

	Options = namedtuple('Options', ['listtags', 
		'listtasks', 
		'listhosts', 
		'syntax', 
		'connection',
		'module_path', 
		'forks', 
		'remote_user', 
		'private_key_file',
		'ssh_common_args', 
		'ssh_extra_args', 
		'sftp_extra_args', 
		'scp_extra_args', 
		'become', 
		'become_method', 
		'become_user', 
		'verbosity', 
		'ask_sudo_pass',
		'ask_su_pass',
		'check'])

	options = Options(
		listtags=False, 
		listtasks=False, 
		listhosts=False, 
		syntax=False, 
		connection='ssh', 
		module_path=None, 
		forks=100, 
		remote_user='kds', 
		private_key_file=None, 
		ssh_common_args=None, 
		ssh_extra_args=None, 
		sftp_extra_args=None, 
		scp_extra_args=None, 
		become=False, 
		become_method=None, 
		become_user='root', 
		verbosity=None, 
		ask_sudo_pass=True,
		ask_su_pass=True,
		check=False)

	#variable_manager.extra_vars = {'hosts': 'mywebserver'}

	#print extras
	#variable_manager.extra_vars = 
	#variable_manager.extra_vars = load_extra_vars(loader=loader, options=options)


	passwords = {'become_pass': '11'}

	pbex = PlaybookExecutor(
		playbooks=[playbook_path],
		inventory=inventory, 
		variable_manager=variable_manager, 
		loader=loader, 
		options=options, 
		passwords=passwords)

	# Maybe do something with stats here? If you want!

	results = pbex.run()

	
		
	