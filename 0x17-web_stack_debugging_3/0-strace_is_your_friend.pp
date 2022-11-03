# Web Stack Debugging, fix syntax error

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => ['/usr/bin', '/bin']
}