#!/usr/bin/env tarantool


local function init()
    link = box.schema.space.create('link')
    link:format({
             {name = 'id', type = 'string'},
             {name = 'original', type = 'string'},
             {name = 'short', type = 'string'}
    })

    link:create_index('primary', {
             type = 'hash',
             parts = {'id'}
             })

    link:create_index('short_index', {
             type = 'hash',
             parts = {'short'},
             unique = true
             })
end


box.cfg{listen = 3301}
box.once('init', init)