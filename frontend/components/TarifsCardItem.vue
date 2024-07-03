<script setup>
import axios from "axios";

const props = defineProps({
  id: Number,
  name: String,
  price: Number,
  minutes: Number,
  gb: Number,
  /* isLoading: Boolean, */
  img: String,
  bonus: String,
  sms: Number,
  link: String,
  descr: String,
  speed: String,
  tv: Number,
  operator: String,
  isFavorite: Boolean,
});

const localFavorite = ref(props.isFavorite);

const { id, isFavorite } = toRefs(props);

const isLoading = inject("isLoading");

const addFavorite = async () => {
  try {
    const response = await axios.put(
      `http://127.0.0.1:8000/api/v1/mobile/${id.value}/favorite/`,
      {
        isFavotite: !isFavorite.value,
      }
    );
    localFavorite.value = !localFavorite.value;
  } catch (error) {
    console.error("An error occurred:", error);
  }
};
</script>

<template>
  <li
    class="card-li relative flex flex-col bg-white rounded-2xl shadow-lg m-5 px-7 pt-5 box-border hover:translate-y-[-5px] hover:shadow-2xl transition-all card-item pb-20"
  >
    <button
      @click="addFavorite"
      v-if="!isLoading"
      class="absolute top-5 right-5 w-5 h-5"
    >
      <img
        :src="localFavorite ? '/heart.png' : '/heart-outline.png'"
        alt="heart"
      />
    </button>
    <h3
      v-if="!isLoading"
      class="head bg-clip-text bg-gradient-to-l from-indigo-500 to-violet-500 text-2xl font-bold"
    >
      {{ operator }}
    </h3>
    <h3 v-else class="skeleton block w-1/2 h-10 bg-[#ededed] rounded-2xl"></h3>
    <p v-if="!isLoading" class="text-sm font-semibold mt-3 text-slate-900">
      <span class="text-5xl text-slate-900 font-bold -mr-1">{{ price }} ₽</span
      >/месяц
    </p>
    <div
      v-else
      class="skeleton block w-full h-14 mt-3 bg-[#ededed] rounded-2xl"
    ></div>
    <h4 v-if="!isLoading" class="text-sm font-bold text-slate-600 mt-3">
      Тариф "{{ name }}"
    </h4>
    <div
      v-else
      class="skeleton block w-1/2 h-6 mt-3 bg-[#ededed] rounded-2xl"
    ></div>
    <ul v-if="!isLoading" class="flex flex-col mt-3 w-full relative">
      <div v-if="speed">
        <li class="feature mb-2 font-semibold text-sm text-slate-900">
          {{ speed }}
        </li>
      </div>
      <div v-if="gb">
        <li
          v-if="gb !== 99999"
          class="feature mb-2 font-semibold text-sm text-slate-900"
        >
          {{ gb }} ГБ
        </li>
        <li
          v-else
          class="feature mb-2 font-semibold text-base text-slate-900 flex"
        >
          <img class="h-6 mr-2" src="/infinity.png" alt="infinity" />
          <span>ГБ</span>
        </li>
      </div>
      <div v-if="minutes">
        <li
          v-if="minutes !== 99999"
          class="feature mb-2 font-semibold text-sm text-slate-900"
        >
          {{ minutes }} минут
        </li>
        <li
          v-else
          class="feature mb-2 font-semibold text-sm text-slate-900 flex"
        >
          <img src="/infinity.png" class="h-6 mr-2" alt="infinity" />
          <span>минут</span>
        </li>
      </div>
      <div v-if="tv">
        <li class="feature mb-2 font-semibold text-sm text-slate-900">
          {{ tv }} ТВ
        </li>
      </div>
      <div v-if="sms">
        <li
          v-if="sms !== 99999"
          class="feature mb-2 font-semibold text-sm text-slate-900"
        >
          {{ sms }} СМС
        </li>
        <li
          v-else
          class="feature mb-2 font-semibold text-sm text-slate-900 flex"
        >
          <img src="/infinity.png" class="h-6 mr-2" alt="infinity" />
          <span>СМС</span>
        </li>
      </div>

      <div v-if="bonus" class="flex items-center w-full trigger cursor-pointer">
        <div
          class="trigger feature mb-2 feature-bonus font-semibold text-sm text-slate-900 underline underline-offset-2 decoration-dashed"
        >
          {{ bonus }}
        </div>
        <div class="h-4 w-4 ml-1 mb-2">
          <svg
            class="h-4 w-4 cursor-pointer"
            xmlns="http://www.w3.org/2000/svg"
            x="0px"
            y="0px"
            width="100"
            height="100"
            viewBox="0 0 26 26"
          >
            <path
              d="M 13 1.1875 C 6.476563 1.1875 1.1875 6.476563 1.1875 13 C 1.1875 19.523438 6.476563 24.8125 13 24.8125 C 19.523438 24.8125 24.8125 19.523438 24.8125 13 C 24.8125 6.476563 19.523438 1.1875 13 1.1875 Z M 15.460938 19.496094 C 14.851563 19.734375 14.367188 19.917969 14.003906 20.042969 C 13.640625 20.167969 13.222656 20.230469 12.742188 20.230469 C 12.007813 20.230469 11.433594 20.050781 11.023438 19.691406 C 10.617188 19.335938 10.414063 18.878906 10.414063 18.324219 C 10.414063 18.109375 10.429688 17.890625 10.460938 17.667969 C 10.488281 17.441406 10.539063 17.191406 10.605469 16.90625 L 11.367188 14.21875 C 11.433594 13.960938 11.492188 13.71875 11.539063 13.488281 C 11.585938 13.257813 11.605469 13.046875 11.605469 12.855469 C 11.605469 12.515625 11.535156 12.273438 11.394531 12.140625 C 11.25 12.003906 10.980469 11.9375 10.582031 11.9375 C 10.386719 11.9375 10.183594 11.96875 9.976563 12.027344 C 9.769531 12.089844 9.59375 12.148438 9.445313 12.203125 L 9.648438 11.375 C 10.144531 11.171875 10.621094 11 11.078125 10.855469 C 11.53125 10.710938 11.964844 10.636719 12.367188 10.636719 C 13.097656 10.636719 13.664063 10.816406 14.058594 11.167969 C 14.453125 11.519531 14.652344 11.980469 14.652344 12.542969 C 14.652344 12.660156 14.640625 12.867188 14.613281 13.160156 C 14.585938 13.453125 14.535156 13.722656 14.460938 13.972656 L 13.703125 16.652344 C 13.640625 16.867188 13.585938 17.113281 13.535156 17.386719 C 13.488281 17.660156 13.464844 17.871094 13.464844 18.011719 C 13.464844 18.367188 13.542969 18.613281 13.703125 18.742188 C 13.859375 18.871094 14.136719 18.933594 14.53125 18.933594 C 14.714844 18.933594 14.921875 18.902344 15.15625 18.839844 C 15.386719 18.773438 15.554688 18.71875 15.660156 18.667969 Z M 15.324219 8.617188 C 14.972656 8.945313 14.546875 9.109375 14.050781 9.109375 C 13.554688 9.109375 13.125 8.945313 12.769531 8.617188 C 12.414063 8.289063 12.238281 7.890625 12.238281 7.425781 C 12.238281 6.960938 12.417969 6.558594 12.769531 6.226563 C 13.125 5.894531 13.554688 5.730469 14.050781 5.730469 C 14.546875 5.730469 14.972656 5.894531 15.324219 6.226563 C 15.679688 6.558594 15.855469 6.960938 15.855469 7.425781 C 15.855469 7.890625 15.679688 8.289063 15.324219 8.617188 Z"
            ></path>
          </svg>
        </div>
      </div>
      <div class="info-block shadow-xl">
        <span class="text-sm">
          {{ descr }}
        </span>
      </div>
    </ul>

    <div
      v-else
      class="skeleton block w-full mt-3 bg-[#ededed] rounded-2xl h-24"
    ></div>

    <button
      v-if="!isLoading"
      class="block absolute bottom-5 w-10/12 inset-x-2/4 -translate-x-1/2 bg-gradient-to-r from-indigo-500 to-violet-500 rounded-xl text-white h-12 font-bold text-base transition-all ease-in-out"
    >
      <a class="w-full" :href="link">Оформить</a>
    </button>

    <button
      v-else
      class="block absolute bottom-5 w-10/12 inset-x-2/4 -translate-x-1/2 bg-gradient-to-r from-indigo-500 to-violet-500 mt-3 rounded-xl text-white h-12 font-bold text-base transition-all ease-in-out disabled:from-slate-300 disabled:to-slate-300 disabled:cursor-not-allowed"
      disabled
    >
      <a class="w-full" :href="link">Оформить</a>
    </button>
  </li>
</template>

<style scoped>
.feature {
  position: relative;
  padding-left: 20px;
}
.feature::before {
  content: "";
  background: url("/vector.svg") center center/contain no-repeat;
  display: block;
  position: absolute;
  left: 0;
  top: 50%;
  transform: translateY(-50%);
  width: 15px;
  height: 15px;
  margin-right: 5px;
}
.feature-bonus::before {
  content: "";
  background: url("/bonus.svg") center center/contain no-repeat;
  display: block;
  position: absolute;
  left: 0;
  top: 50%;
  transform: translateY(-50%);
  width: 15px;
  height: 15px;
  margin-right: 5px;
}
.head {
  color: transparent;
}

.skeleton {
  position: relative;
}
.skeleton::before {
  content: "";
  width: 100%;
  height: 100%;
  border-radius: 15px;
  position: absolute;
  left: 0;
  top: 0;
  background: linear-gradient(90deg, #ededed 0%, #f7f7f7 50%, #ededed 100%);
  background-size: 200% 100%;
  animation: loading 2s ease-in-out infinite;
}

.info-block {
  position: absolute;
  display: none;
  left: 50%;
  transform: translateX(-50%);
  bottom: 35px;
  min-width: 360px;
  min-height: 0px;
  background-color: #ffffff;
  padding: 15px;
  border: 1px solid #ccc;
  border-radius: 10px;
  animation: info 0.3s ease-in-out;
  z-index: 100;
}

.trigger:hover + .info-block {
  display: block;
  z-index: 100;
}

.trigger:hover ~ .info-block {
  display: block;
  z-index: 100;
}

.info-block p {
  font-size: 16px;
  line-height: 1.5;
  margin-bottom: 15px;
}

.info-block a {
  color: #007bff;
  text-decoration: underline;
}

.info-block a:hover {
  color: #0056b3;
  text-decoration: none;
}

.card-li {
  animation: card-li 0.5s ease-in-out forwards;
}

@keyframes card-li {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}

@keyframes loading {
  0% {
    background-position: 0 0;
  }
  50% {
    background-position: 100% 0;
  }
  100% {
    background-position: 0 0;
  }
}

@keyframes info {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}
</style>
