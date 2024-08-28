---
title: Run INT8 TFlite Model on ASIP

---

# Run INT8 TFlite Model on ASIP

## Edit arena.cc file
The original code in arena.cc is aligned(32), you need to change it to 8 as shown below to run int8 model.
```cpp
uint8_t tensor_arena[kTensorArenaSize] __attribute__((aligned(8)));
```

## Generate model_data.cc file
Take vww_96_int8.tflite for example.
```bash
 $ cd mlperf_model
 $ xxd -i vww_96_int8.tflite > model.cc
 $ (echo -ne "#include \"model/model_data.h\"\nalignas(16) "; cat model.cc) > model_data.cc
 $ sed -i -E 's/(unsigned\s.*\s).*(_len|\[\])/const \1model\2/g' model_data.cc
 $ mv model_data.cc ../model/model_data.cc
 $ cd ..
 $ python3 gen_prx.py trv32p3 ~/V-2023.12/linux64/examples/trv/trv32p3/lib
 $ chessmk -j12 tflm.prx
```
Open the chessde IDE and run the project