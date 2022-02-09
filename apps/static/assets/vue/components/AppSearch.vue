<template>
    <div id="table">
        <sequential-entrance>
            <div class="btn" v-for="index in 5" :key="index"></div>
        </sequential-entrance>
    </div>
</template>