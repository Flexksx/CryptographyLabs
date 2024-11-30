{
  description = A simple flake for a Rust project with rustup and cargo;

  inputs = {
    nixpkgs.url = github:NixOS/nixpkgs;
    flake-utils.url = github:numtide/flake-utils;
  };

  outputs = { self, nixpkgs, flake-utils }: 
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };
      in {
        devShell = pkgs.mkShell {
          name = rust-dev-shell;
          buildInputs = [
            pkgs.rustup
            pkgs.cargo
          ];
        };
      });
}

