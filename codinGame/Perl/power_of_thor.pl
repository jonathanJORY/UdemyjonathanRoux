use strict;
use warnings;
use 5.32.1;

select(STDOUT); $| = 1;

chomp(my $input = <STDIN>);
my ($lx, $ly, $tx, $ty) = split / /, $input;

while (<STDIN>) {
    print(($ty>$ly?'N':$ty<$ly?'S':'').($tx>$lx?'W':$tx<$lx?'E':'')."\n");
    $tx += ($lx>$tx) - ($lx<$tx);
    $ty += ($ly>$ty) - ($ly<$ty);
}
