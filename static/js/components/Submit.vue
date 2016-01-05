<template>
    <div class="col-sm-offset-2 col-sm-10">
        <button type="submit" id="${ cid }" class="btn btn-default">${ value }</button>
    </div>
</template>

<script>
    module.exports = {
        props: ['value', 'cid']
    }
</script>
