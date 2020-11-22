.. meta::
    :description: Description of the Nissan Leaf OBD-II diagnostic connector
        including protocols and pin assignments.

.. _diagnostic-connector:

====================
Diagnostic connector
====================

The *Nissan Leaf* is fitted with a :term:`Type A diagnostic connector` as
defined in :term:`ISO 15031-3` or its equivalent :term:`SAE J1962`. Type A
diagnostic connectors have 16 pins arranged in two rows of eight. Nine of the
pins have a mandated designation - with use of the remaining pins being at the
discretion of the vehicle manufacturer.


Location
--------

The *Leaf*'s diagnostic connector is located beneath the steering column as is
seen in :numref:`leaf-diagnostic-connector`.

.. figure:: _static/images/nissan-leaf-diagnostic-connector.*
    :name: leaf-diagnostic-connector
    :alt: Nissan Leaf OBD-II diagnostic connector
    :height: 480
    :width: 640

    *Nissan Leaf* OBD-II vehicle diagnostic connector (mating-end view)


CAN buses
---------

The *Leaf* has three :term:`CAN` buses commonly referred to as: :term:`AV-CAN`,
:term:`EV-CAN`, and :term:`Car-CAN`. The :term:`CAN protocol` used in the
*Leaf* is :term:`ISO 15765-4` CAN (11-bit ID, 500 :term:`kBd`) which is often
abbreviated to "ISO 15765‑4 (CAN 11/500)."

Each CAN bus carries messages relating to a different aspect of the vehicle's
operation:

AV‑CAN |dc-av-can-high|
    Messages related to the display screen.

Car‑CAN |dc-car-can-high|
    Messages related to general vehicle operation including EV related
    messages.

EV‑CAN |dc-ev-can-high|
    Messages related to the battery and drive system.


Contact designation
-------------------

:numref:`leaf-diagnostic-connector-contact-designation` depicts the mating-end
view of the :term:`OBD-II` vehicle diagnostic connector. Colours of the
:term:`CAN` bus symbols are selected to correspond with the colour code of
four-pair ethernet cable.

.. figure:: _static/images/nissan-leaf-diagnostic-connector-pins.*
    :name: leaf-diagnostic-connector-contact-designation
    :alt: Nissan Leaf OBD-II diagnostic connector contact designation
    :height: 120
    :width: 300

    *Nissan Leaf* OBD-II diagnostic connector contact designation (mating-end
    view)

As can be seen in
:numref:`leaf-diagnostic-connector-contact-designation-legend`, the *Leaf* uses
five of the contacts with a mandated designation: chassis ground, signal
ground, Car‑CAN high, Car‑CAN low, and permanent +12 V DC. The designation of
the remaining pins is specific to the *Leaf*: AV‑CAN low, +12 V DC when vehicle
powered on, AV‑CAN high, EV‑CAN low, and EV‑CAN high.

.. table:: *Nissan Leaf* vehicle diagnostic connector contact designation
    :name: leaf-diagnostic-connector-contact-designation-legend
    :widths: auto

    +-----+---------------------+---------------------------------------+
    | Pin | Symbol [1]_         | Designation                           |
    +=====+=====================+=======================================+
    | 1   | |dc-nc|             | No connection                         |
    +-----+---------------------+---------------------------------------+
    | 2   | |dc-nc|             | No connection [2]_                    |
    +-----+---------------------+---------------------------------------+
    | 3   | |dc-av-can-low|     | AV‑CAN low [3]_                       |
    +-----+---------------------+---------------------------------------+
    | 4   | |dc-chassis-ground| | Chassis ground [2]_                   |
    +-----+---------------------+---------------------------------------+
    | 5   | |dc-signal-ground|  | Signal ground [2]_                    |
    +-----+---------------------+---------------------------------------+
    | 6   | |dc-car-can-high|   | Car‑CAN high [2]_                     |
    +-----+---------------------+---------------------------------------+
    | 7   | |dc-nc|             | No connection [2]_                    |
    +-----+---------------------+---------------------------------------+
    | 8   | |dc-power-on|       | +12 V DC when vehicle powered on [3]_ |
    +-----+---------------------+---------------------------------------+
    | 9   | |dc-nc|             | No connection                         |
    +-----+---------------------+---------------------------------------+
    | 10  | |dc-nc|             | No connection [2]_                    |
    +-----+---------------------+---------------------------------------+
    | 11  | |dc-av-can-high|    | AV‑CAN high [3]_                      |
    +-----+---------------------+---------------------------------------+
    | 12  | |dc-ev-can-low|     | EV‑CAN low [3]_                       |
    +-----+---------------------+---------------------------------------+
    | 13  | |dc-ev-can-high|    | EV‑CAN high [3]_                      |
    +-----+---------------------+---------------------------------------+
    | 14  | |dc-car-can-low|    | Car‑CAN low [2]_                      |
    +-----+---------------------+---------------------------------------+
    | 15  | |dc-nc|             | No connection [2]_                    |
    +-----+---------------------+---------------------------------------+
    | 16  | |dc-12vdc|          | Permanent +12 V DC [2]_               |
    +-----+---------------------+---------------------------------------+

.. [1] CAN bus symbol colours correspond to 4-pair ethernet cable colour code.
.. [2] Mandated allocation defined in ISO 15031-3.
.. [3] :cite:`mynissanleaf:can-decoding`.


.. include:: /includes/diagnostic-connector-symbols.rst
