$file_path = '/var/www/html/wp-settings.php'

file { $file_path:
  ensure => file,
}

exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${file_path}",
  path    => ['/bin', '/usr/bin'],
  require => File[$file_path],
}

