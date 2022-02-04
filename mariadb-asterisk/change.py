with open ('/etc/containers/registries.conf', 'r') as f:
  old_data = f.read()

with open ('/etc/containers/registries.conf', 'w') as f:
  new_data = old_data.replace("registries = [\'registry.access.redhat.com\', \'registry.redhat.io\', \'docker.io\']", "registries = [\'docker.io\']")
#  new_data = old_data.replace("registries = [\'docker.io\']","registries = [\'registry.access.redhat.com\', \'registry.redhat.io\', \'docker.io\']")
  f.write(new_data)

exit();
