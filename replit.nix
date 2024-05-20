{pkgs}: {
  deps = [
    pkgs.python39Full
    pkgs.python39Packages.pyodbc
    pkgs.unixODBC
    pkgs.unixODBC.dev
    pkgs.curl
    pkgs.gnupg
  ];

  env = {
    LD_LIBRARY_PATH = "${pkgs.unixODBC}/lib:${pkgs.unixODBC.dev}/lib";
  };
}
