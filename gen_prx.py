import os
import glob
import argparse

def path_to_prx(path: str):
    dirname = os.path.dirname(path)
    filename = os.path.basename(path)
    return f'    <file type="c" name="{filename}" path="{dirname}"/>'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("proc_name", type=str, help="Name of selected processor model")
    parser.add_argument("proc_lib", type=str, help="Path to 'lib' folder of selected processor model")
    args = parser.parse_args()
    proc_name = str(args.proc_name)
    proc_lib = str(args.proc_lib)

    # Get all C/C++ src files
    src_list = sorted([f for f in glob.glob("**/*.cpp", recursive=True) if "mbed-os" not in f])
    src_list += sorted([f for f in glob.glob("**/*.cc", recursive=True) if "mbed-os" not in f])
    src_list += sorted([f for f in glob.glob("**/*.c", recursive=True) if "mbed-os" not in f])
    # To .prx format
    src_list_prx = [path_to_prx(p) for p in src_list]

    head = [
        f'<project name="TFLM" processor="{proc_name}" lib="{proc_lib}">',
        r'    <configuration remove="1" parent="Release"/>',
        r'    <configuration remove="1" parent="Release_LLVM"/>'
        r'    <configuration remove="1" parent="Debug"/>'
    ]
    tail = [
        # '    <option id="bridge.cfg" value="trv32p3_2xstack.bcf" cfg="Release_LLVM_full"/>',
        r'    <option id="cpp.define" value="USE_STREAMS" inherit="1" cfg="Native"/>',
        r'    <option id="cpp.define" value="TF_LITE_STATIC_MEMORY" inherit="1" cfg="Release_LLVM_full"/>',
        r'    <option id="cpp.include" value="{} third_party/flatbuffers/include third_party/gemmlowp examples/hello_world third_party/kissfft third_party/ruy" inherit="1" cfg="Release_LLVM_full"/>',
        r'    <option id="project.name" value="tflm"/>',
        r'    <option id="project.type" value="exe"/>',
        r'</project>'
    ]
    with open("tflm.prx", 'w') as f:
        f.write('\n'.join(head + src_list_prx + tail))
