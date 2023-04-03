# Installs Nginx and creates a custom HTTP header

exec { '/usr/bin/env apt-get -y update' : }
-> package { 'nginx':
   ensure => installed,
}

-> file_line { 'add header' :
   ensure => present,
   line => "\tadd_header X-Served-By ${hostname};",
   path => '/etc/nginx/sites-available/default',
   after => 'server_name _;,
}

-> file { '/var/www/html/index.html' :
   content => 'Hello World!'
}

-> service { 'nginx':
   ensure => running,
}
