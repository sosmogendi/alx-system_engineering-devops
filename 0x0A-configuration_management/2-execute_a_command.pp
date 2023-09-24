# Puppet Manifest to Kill a Process Named 'killmenow'

exec { 'kill_killmenow':
  command     => 'pkill -f killmenow',
  path        => '/bin:/usr/bin:/usr/sbin',
  refreshonly => true,
  subscribe   => File['/alx-system_engineering-devops/0x0A-configuration_management/killmenow'],
  onlyif      => 'pgrep -f killmenow',
  notify      => "Killing process 'killmenow'",
}
