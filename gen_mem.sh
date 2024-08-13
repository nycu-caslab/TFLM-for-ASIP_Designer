full_path=$(readlink -f ${0})

dir_name=$(dirname ${full_path})
parent_dir_name=$(dirname ${dir_name})

prog_name=$(basename ${dir_name})
proc_model=$(basename ${parent_dir_name})

PM_name=ePM
DM_name=eDM

vivado_proj_path="/home/liuyy3364/learning/ASIP/vlog_proj/Trv32_proj/Trv32_proj"

# rm -r ./Release*/
chessmk ${prog_name}.prx -m  -j 20 && chessmk ${prog_name}.prx +H && \
cat Release_LLVM_full/${prog_name}.${PM_name} > ${vivado_proj_path}.srcs/sources_1/imports/memfile/PM.mem && \
cat Release_LLVM_full/${prog_name}.${DM_name} > ${vivado_proj_path}.srcs/sources_1/imports/memfile/DM.mem && \
cat Release_LLVM_full/${prog_name}.${PM_name} > ${vivado_proj_path}.sim/sim_1/behav/xsim/PM.mem && \
cat Release_LLVM_full/${prog_name}.${DM_name} > ${vivado_proj_path}.sim/sim_1/behav/xsim/DM.mem && \
cat Release_LLVM_full/${prog_name}.${PM_name} > ${vivado_proj_path}.srcs/ASIP/${proc_model}/hdl/${proc_model}_vlog/data.PM && \
cat Release_LLVM_full/${prog_name}.${DM_name} > ${vivado_proj_path}.srcs/ASIP/${proc_model}/hdl/${proc_model}_vlog/data.DM
