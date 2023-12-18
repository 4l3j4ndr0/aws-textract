<template>
  <q-page class="q-pa-md example-row-equal-width">
    <div class="row q-gutter-md q-pa-md">
      <div class="col-md-4 q-gutter-lg">
        <q-input
          v-model="apiGatewayUrl"
          label="Api Gateway URL"
          lazy-rules
          :rules="[
            (val) =>
              (val && val.length > 0) || 'The api gateway endpoint is required',
          ]"
        >
          <template v-slot:prepend>
            <q-icon name="language" />
          </template>
        </q-input>
        <q-uploader
          label="Upload the expense image"
          accept="image/png,image/jpeg"
          color="primmary"
          flat
          bordered
          :multiple="false"
          @added="(files) => uploadFile(files)"
        />
        <q-btn
          color="primary"
          label="Extract information"
          v-if="apiGatewayUrl && base64Data"
          @click="extractInformationRequest"
          :loading="loading"
        />
      </div>

      <div class="col-md-7">
        <h5><b>Information extracted using Textract expense analysis</b></h5>
        <q-separator size="3px" />
        <div class="row q-pt-lg">
          <q-chip
            outline
            color="primary"
            text-color="white"
            v-for="item in textractData"
          >
            {{ item.label }}:{{ item.value }}
          </q-chip>
        </div>
      </div>
    </div>
  </q-page>
</template>

<script>
import { defineComponent, ref } from "vue";
import axios from "axios";
export default defineComponent({
  name: "IndexPage",
  setup() {
    const apiGatewayUrl = ref(null);
    const loading = ref(false);
    const base64Data = ref(null);
    const textractData = ref([]);
    const convertBase64 = (file) => {
      return new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onload = () => resolve(reader.result);
        reader.onerror = reject;
      });
    };

    const extractInformationRequest = () => {
      loading.value = true;
      axios
        .post(`${apiGatewayUrl.value.trim()}`, {
          base64_image: base64Data.value,
        })
        .then((response) => {
          textractData.value = response.data;
          loading.value = false;
        })
        .catch((e) => {
          console.log("ERROR REQUEST:::::", e);
          loading.value = false;
        });
    };

    const uploadFile = (files) => {
      convertBase64(files[0]).then((b64) => {
        base64Data.value = b64;
      });
    };

    return {
      uploadFile,
      apiGatewayUrl,
      extractInformationRequest,
      base64Data,
      textractData,
      loading,
    };
  },
});
</script>
