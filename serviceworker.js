var CACHE_NAME = 'my-syte-cache-v1';
var urlsToCache = [
    '/',
    '/static/blog/css/style.css',
    '/static/blog/imagenes/bomberos_quilpue.jpg',
];

self.addEventListener('install', function(event) {
  // Perform install steps
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
  );
});

self.addEventListener('fetch', function(event) {
    event.respondWith(
        fetch(event.request)
        .then(function(resul){
          return caches.open(CACHE_NAME)
          .then(function(c){
            c.put(event.request.url, resul.clone())
            return resul;

          })

        })
        .catch(function(e){
          return caches.match(event.request)
        })
    );
});

