<template>
  <div class="home">
    <h1>{{ msg }}</h1>
    <alert :message="message" v-if="showMessage"></alert>
    <b-button
      type="button"
      size="lg"
      variant="outline-success"
      v-b-modal.selection-modal
    >
      Load new Data
    </b-button>
    <br /><br />

    <b-modal
      ref="selectionModal"
      id="selection-modal"
      title="Load new data"
      header-bg-variant="light"
      body-bg-variant="light"
      hide-footer
    >
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        <b-form-group
          id="form-sel-group"
          label="Select:"
          label-for="form-sel-input"
        >
          <b-form-select
            v-model="selectionForm.choice"
            :options="choices"
            required
          ></b-form-select>
        </b-form-group>
        <br />

        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>

    <img :src="initializeChart()" class="img-chart" alt="chart" />
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';

export default {
  name: "Chart",
  props: {
    msg: String,
  },
  data() {
    return {
      selectionForm: {
        choice: null,
      },
      //Configure this choice to make it what you want for the dropdown
      choices: [
        { value: null, text: "Please select" },
        { value: "Choice 1", text: "Choice 1" },
        { value: "Choice 2", text: "Choice 2" },
        { value: "Choice 3", text: "Choice 3" },
      ],
      message: "",
      showMessage: false,
      endpoint: "http://localhost:5000/",
      imageURL: "chart",
    };
  },
    components: {
    alert: Alert,
  },
  methods: {


    initializeChart(){
        return this.endpoint+this.imageURL;
    },
    submitSelection(payload) {
      const path = "http://localhost:5000/loadChart";
      axios
        .post(path, payload)
        .then((res) => {
          if (res != null){
            this.message = "Loaded!";
            this.showMessage = true;
            this.imageURL = res.data.imageURL;
          }
          
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.message = "Error";
        });
    },
    initForm() {
      this.selectionForm.choice = null;
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.selectionModal.hide();
      const payload = {
        choice: this.selectionForm.choice,
      };
      this.submitSelection(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.selectionModal.hide();
      this.initForm();
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
