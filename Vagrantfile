config.vm.provision "ansible" do |ansible|
    ansible.playbook = "ansible/provision.yml"
    ansible.inventory_path = "ansible/inventories/dev_servers"
    ansible.limit = 'all'
end
