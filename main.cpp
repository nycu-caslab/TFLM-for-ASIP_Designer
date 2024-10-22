/* Copyright 2020 The MLPerf Authors. All Rights Reserved.
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
==============================================================================*/
/// \file
/// \brief Main function to run benchmark on device.

#include "api/internally_implemented.h"
#include "api/submitter_implemented.h"

#define EXEC_CNT 1

extern  char model_name[];
extern  char compile_time[];

extern uint32_t cc_min;
extern uint32_t cc_max;
extern int64_t  cc_tot;

uint32_t tot_time = 0;
uint32_t lat_min = UINT32_MAX;
uint32_t lat_max = 0;

int main(int argc, char *argv[]) {
  // MLPerf Tiny initialization
  ee_benchmark_initialize();

  // hard-coded MLPerf command
  char cmd[] = "infer 1 0%";
  // Directly feed infer cmd to MLPerf Tiny's CLI
  // Run for EXEC_CNT times
  for(int j = 0; j < EXEC_CNT; j++){
    for(int i = 0; i < strlen(cmd); i++) {
      ee_serial_callback(cmd[i]);
    }
  }

  return 0;
}
