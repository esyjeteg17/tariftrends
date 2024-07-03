<template>
  <div>
    <Header />
    <!-- <Banner v-if="!user" /> -->
    <div class="w-10/12 mx-auto">
      <slot />
    </div>
  </div>
</template>

<script setup>
import { useAuthStore } from "~/store/index";

const authStore = useAuthStore();
const user = computed(() => authStore.user);
</script>
