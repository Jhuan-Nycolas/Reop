{
  stdenv,
  python3,
}:
stdenv.mkDerivation {
  name = "reop";

  src = ./dist;

  buildInputs = [python3];

  installPhase = ''
    mkdir -p $out/bin
    cp -r $src/reop $out/bin/
  '';
}
