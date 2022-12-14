# Web Stack debugging increase holberton user FD limits
exec { 'Change-hoberton-user-limits':
  environment => ['DIR=/etc/security/limits.conf',
                  'OHARD=hard nofile 5',
                  'NHARD=hard nofile 50000',
                  'OSOFT=soft nofile 4',
                  'NSOFT=soft nofile 40000'],
  command     => 'sudo sed -i "s/$OHARD/$NHARD/" $DIR; sudo sed -i "s/$OSOFT/$NSOFT/" $DIR',
  path        => ['/usr/bin', '/bin'],
}