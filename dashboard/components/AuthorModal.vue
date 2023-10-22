<template>
  <b-modal 
    id="modal-author" 
    ref="modal" 
    title="Add/Edit Author Info" 
    @show="resetModal" 
    @hidden="resetModal"
    @ok="handleOk">
    <form ref="form" @submit.stop.prevent="handleSubmit">
      <b-form-group label="Author Name" label-for="name-input" invalid-feedback="Name is required" :state="nameState">
        <b-form-input id="name-input" v-model="name" :state="nameState" required></b-form-input>
      </b-form-group>
      <b-form-group label="Books" label-for="name-input">
        <b-table 
          striped 
          hover 
          :items="items" 
          :busy="isBusy" 
          select-mode="single" 
          selectable 
          outlined
          @row-selected="onRowSelected">
          <template #table-busy>
            <div class="text-center text-danger my-2">
              <b-spinner class="align-middle"></b-spinner>
              <strong>Loading...</strong>
            </div>
          </template>
        </b-table>
      </b-form-group>
    </form>
  </b-modal>
</template>
  
<script>
export default {
  name: 'AuthorModal',
  props: {
    author: {
      type: Number,
      default: -1
    },
  },
  data() {
    return {
      isBusy: false,
      name: '',
      nameState: null,
      submittedNames: [],
      items: [
        { age: 40, first_name: 'Dickerson', last_name: 'Macdonald' },
        { age: 21, first_name: 'Larsen', last_name: 'Shaw' },
        { age: 89, first_name: 'Geneva', last_name: 'Wilson' },
        { age: 38, first_name: 'Jami', last_name: 'Carney' }
      ]
    }
  },
  methods: {
    checkFormValidity() {
      const valid = this.$refs.form.checkValidity()
      this.nameState = valid
      return valid
    },
    resetModal() {
      this.name = ''
      this.nameState = null
    },
    handleOk(bvModalEvent) {
      // Prevent modal from closing
      bvModalEvent.preventDefault()
      // Trigger submit handler
      this.handleSubmit()
    },
    handleSubmit() {
      // Exit when the form isn't valid
      if (!this.checkFormValidity()) {
        return
      }
      // Push the name to submitted names
      this.submittedNames.push(this.name)
      // Hide the modal manually
      this.$nextTick(() => {
        this.$bvModal.hide('modal-prevent-closing')
      })
    },
    onRowSelected() {
      
    }
  }
}
</script>