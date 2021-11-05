#!/usr/bin/env tarantool


local function init()
    link = box.schema.space.create('link1')
    link:format({
             {name = 'id', type = 'unsigned'},
             {name = 'original', type = 'string'},
             {name = 'short', type = 'string'}
    })

    link:create_index('primary', {
             type = 'hash',
             parts = {'id'}
             })

    link:create_index('original_index', {
             type = 'hash',
             parts = {'original'}
             })

    link:create_index('short_index', {
             type = 'hash',
             parts = {'short'}
             })
end


box.cfg{listen = 3301}
box.once('init', init)