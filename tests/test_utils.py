import os
import subprocess
import numpy

class SubroutineTester:
    def __init__(self, subroutine_name: str, binary_origin: int = 0x1000, addrio: int = 0xff) -> None:
        self.subroutine_name = subroutine_name
        self.binary_origin = binary_origin
        self.addrio = addrio

    def initialise(self):
        test_file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "subroutines", self.subroutine_name)
        subroutines_path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir))
        binaries_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "bin")
        subroutine_name = os.path.splitext(os.path.basename(test_file_path))[0]
        binary_path = os.path.join(binaries_path, subroutine_name)

        if not os.path.exists(binaries_path):
            os.mkdir(binaries_path)

        subprocess.run(["vasm6502_oldstyle",
                        "-Fbin",
                        "-dotdir",
                        f"-DORIGIN={self.binary_origin}",
                        f"-DADDRIO={self.addrio}",
                        "-o",
                        f"{binary_path}",
                        test_file_path],
                        stdout=subprocess.DEVNULL)

    def run_test(self, *args: numpy.float32) -> numpy.float32:
        test_file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "subroutines", self.subroutine_name)
        binaries_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "bin")
        subroutine_name = os.path.splitext(os.path.basename(test_file_path))[0]
        binary_path = os.path.join(binaries_path, subroutine_name)

        execute = subprocess.Popen(["run6502",
                                    "-l",
                                    f"{self.binary_origin:x}",
                                    f"{binary_path}",
                                    "-R",
                                    f"{self.binary_origin:x}",
                                    "-M",
                                    f"{self.addrio:x}",
                                    "-X",
                                    "0"],
                                    stdin=subprocess.PIPE,
                                    stdout=subprocess.PIPE)

        input = b''.join(map(lambda b: b[::-1], map(numpy.float32.tobytes, args)))
        output = execute.communicate(input=input)[0]

        return numpy.frombuffer(output, dtype=numpy.float32)[0]