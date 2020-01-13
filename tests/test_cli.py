import subprocess

def test_cli_usage():
    cmd = ["oneproj"]
    try:
        out = subprocess.check_output(cmd,
                                      stderr=subprocess.STDOUT,
                                      shell=True,
                                      universal_newlines=True)
    except subprocess.CalledProcessError as e:
        pass
    else:
        # if no error raised, check the returned string
        assert len(out) > 0 and "one" in out.lower(), \
            "Incorrect message returned from CLI"