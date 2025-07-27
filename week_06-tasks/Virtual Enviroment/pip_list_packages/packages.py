import pkg_resources

installed_packages = pkg_resources.working_set
package_list = sorted(["{}=={}".format(pkg.key, pkg.version) for pkg in installed_packages])

print("Installed pip packages:")
for package in package_list:
    print(package)
