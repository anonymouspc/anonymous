1. module imports cycle.
2. Module("a") depends on Package("a") depends on Module("a").
  - You cannot use Module("a") **sync** depends on Package("a"), because they run on 2 different threads.
