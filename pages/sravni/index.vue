<script setup>
const category = ref("mobile");
const filter = ref("");
const operator = ref([]);
const search = ref("");

const gigabytes = ref([0, 99999]);

const filtersLoading = ref(false);

const isLoading = ref(true);

const prices = reactive({
  min: "",
  max: "",
});

const firstPrices = {
  min: "",
  max: "",
};

const operators = ref([]);

const showSort = ref(false);

const sortIsActive = ref(false);

const networkError = ref(false);

const setShowSort = (e) => {
  if (e.target.classList.contains("show-sort")) {
    showSort.value = !showSort.value;
    sortIsActive.value = !sortIsActive.value;
  } else {
    showSort.value = false;
    sortIsActive.value = false;
  }
};

const setOperators = (items) => {
  const uniqueOperators = items.filter(
    (item, index, self) =>
      index === self.findIndex((t) => t.operator === item.operator)
  );

  operators.value = uniqueOperators.map((item) => item.operator);
};

const setFilter = (e) => {
  filter.value = e.target.value;
};

const setPrices = (e) => {
  if (e.target.id === "pricemin") {
    prices.min = e.target.value;
    document.querySelectorAll(".priceinp").forEach((el) => {
      el.checked = false;
    });
  }
  if (e.target.id === "pricemax") {
    prices.max = e.target.value;
    document.querySelectorAll(".priceinp").forEach((el) => {
      el.checked = false;
    });
  }
  if (e.target.id === "1") {
    prices.min = firstPrices.min;
    prices.max = `${Math.round(firstPrices.max / 5 / 100) * 100}`;
    document.querySelectorAll(".price-input").forEach((el) => {
      el.value = "";
    });
  }
  if (e.target.id === "1-2") {
    e.target.value = "";
    prices.min = `${Math.round(firstPrices.max / 5 / 100) * 100}`;
    prices.max = `${2 * Math.round(firstPrices.max / 5 / 100) * 100}`;
    document.querySelectorAll(".price-input").forEach((el) => {
      el.value = "";
    });
  }
  if (e.target.id === "2-3") {
    prices.min = `${Math.round((2 * firstPrices.max) / 5 / 100) * 100}`;
    prices.max = `${Math.round((3 * firstPrices.max) / 5 / 100) * 100}`;
    document.querySelectorAll(".price-input").forEach((el) => {
      el.value = "";
    });
  }
  if (e.target.id === "3-4") {
    prices.min = `${Math.round((3 * firstPrices.max) / 5 / 100) * 100}`;
    prices.max = `${Math.round((4 * firstPrices.max) / 5 / 100) * 100}`;
    document.querySelectorAll(".price-input").forEach((el) => {
      el.value = "";
    });
  }
  if (e.target.id === "more") {
    prices.min = `${Math.round((4 * firstPrices.max) / 5 / 100) * 100}`;
    prices.max = firstPrices.max;
    document.querySelectorAll(".price-input").forEach((el) => {
      el.value = "";
    });
  }
};

const resetPrices = () => {
  prices.min = firstPrices.min;
  prices.max = firstPrices.max;
  document.querySelectorAll(".price-input").forEach((el) => {
    el.value = "";
  });
  document.querySelectorAll(".priceinp").forEach((el) => {
    el.checked = false;
  });
};

const setOperator = (e) => {
  if (e.target.checked) {
    operator.value.push(e.target.value);
  }
  if (!e.target.checked) {
    operator.value.splice(operator.value.indexOf(e.target.value), 1);
  }
};

const setSearch = (e) => {
  search.value = e.target.value;
};

const setFirstPrices = (items) => {
  if (items.length === 0) {
    return;
  }
  const maxPrice = items.reduce(
    (max, item) => (item.price > max ? item.price : max),
    0
  );

  prices.max = maxPrice;

  const minPrice = items.reduce(
    (min, item) => (item.price < min ? item.price : min),
    items[0].price
  );

  prices.min = minPrice;

  firstPrices.min = minPrice;
  firstPrices.max = maxPrice;
};

provide("filter", filter);
provide("category", category);
provide("operator", operator);
provide("search", search);
provide("prices", prices);
provide("operators", operators);
provide("showSort", showSort);
provide("sortIsActive", sortIsActive);
provide("maxPrice", prices.max);
provide("isLoading", isLoading);
provide("firstPrices", firstPrices);
provide("filtersLoading", filtersLoading);
provide("networkError", networkError);
provide("gigabytes", gigabytes);
</script>

<template>
  <div
    @scroll="setShadow"
    @click="(e) => setShowSort(e)"
    class="wrapper relative mt-28"
  >
    <div class="fixed w-60">
      <Filters
        v-if="!filtersLoading"
        :set-filter="setFilter"
        :set-operator="setOperator"
        :set-search="setSearch"
        :set-prices="setPrices"
        :reset-prices="resetPrices"
      />
    </div>

    <div class="w-full pl-72">
      <ChoiceTabs :category="category" />
      <TarifsCardList
        :set-operators="setOperators"
        :set-filter="setFilter"
        :set-show-sort="setShowSort"
        :set-first-prices="setFirstPrices"
      />
    </div>
  </div>
</template>

<style scoped>
.wrapper {
  grid-template-columns: 1fr 6fr;
}
</style>
