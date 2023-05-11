# Puppet script to replace a line in a file

# File path
$file_path = '/var/www/html/wp-settings.php'

# Ensure the file exists
file { $file_path:
  ensure => file,
}

# Execute sed command to replace the line
exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${file_path}",
  path    => ['/bin', '/usr/bin'],
  require => File[$file_path],
}
