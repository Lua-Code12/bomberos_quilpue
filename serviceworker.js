//instalación e interceptación

if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('bomberos_quilpue/serviceworker.js')
        .then((reg) => {
          console.log('Service worker registered.', registration);
        });
  });
}

var CACHE_NAME = 'my-site-cache-v1';
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
    .then((result)=>{
      return caches.open(CACHE_NAME)
      .then(function(c) {
        c.put(event.request.url, result.clone())
        return result;
      })
      
    })
    .catch(function(e){
        return caches.match(event.request)
    })


   
  );
});

function newFunction() {
  <script src="/lib/jquery.min.js"></script>
    ,
    <script src="/lib/jquery.plugin.js"></script>;
}

