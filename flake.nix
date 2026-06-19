{
  description = "Django + Vue dev env";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };
      in {
        devShells.default = pkgs.mkShell {
          packages = with pkgs; [
            python314
            uv

            nodejs_20
            pnpm

            git
          ];

          shellHook = ''
            echo "DevShell activo (Django + Vue)"

            # opcional: fuerza uv a usar venv local del proyecto
            export UV_PROJECT_ENVIRONMENT=.venv
          '';
        };
      });
}