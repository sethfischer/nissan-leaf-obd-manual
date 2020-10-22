.. meta::
    :description: Glossary of terms used in the Nissan Leaf OBD-II guide.


========
Glossary
========

.. glossary::
    :sorted:

    AV-CAN
        Name of the *Nissan Leaf* :term:`CAN` bus which carries predominantly
        infotainment data. Exposed on pins 3 and 11 of the
        :term:`diagnostic connector`.

    CAN
        Abbreviation for :term:`controller area network`.

    CAN protocol
        Transport protocol (layer 4) and network (layer 3) protocol implemented
        on a :term:`CAN` bus. The :term:`OBD-II` protocol used by the
        *Nissan Leaf* is :term:`ISO 15765-4` CAN (11-bit ID, 500 :term:`kBd`).

    Car-CAN
        Name of the *Nissan Leaf* :term:`CAN` bus exposed on pins 6 and 14 of
        the :term:`diagnostic connector`.

    communication protocol
        A system of rules that allow two or more entities of a communications
        system to transmit information.

    controller area network
        A vehicle bus standard designed to allow microcontrollers and devices
        to communicate without a host computer.

    diagnostic connector
        A physical connector used to access :term:`on-board diagnostics` and
        data streams. The :term:`OBD-II` diagnostic connector (defined in
        :term:`ISO 15031-3`) is a 16-pin connector which, on a *Nissan Leaf*,
        is located beneath the steering column.

    EV-CAN
        Name of the *Nissan Leaf* :term:`CAN` bus which carries data related to
        the traction battery and electric motor drive system. Exposed on pins 3
        and 11 of the :term:`diagnostic connector`.

    ISO 15031-3
        Document published by the
        `International Organization for Standardization`_ (ISO) titled *Road
        vehicles — Communication between vehicle and external equipment for
        emissions-related diagnostics — Part 3: Diagnostic connector and
        related electrical circuits: Specification and use*.

    ISO 15765-4
        Document published by the
        `International Organization for Standardization`_ (ISO) titled *Road
        vehicles — Diagnostic communication over Controller Area Network
        (DoCAN) — Part 4: Requirements for emissions-related systems*.

    kBd
        Abbreviation for kilobaud where 1 kBd = 1000 Bd (baud).

    OBD-II
        Abbreviation for revision two of the :term:`on-board diagnostics`
        standardised interface.

    on-board diagnostics
        A term referring to a vehicle's self-diagnostic and reporting
        capability.

    SAE J1962
        Document published by `SAE International`_ titled *Diagnostic Connector
        Equivalent to ISO/DIS 15031-3:December 14, 2001*. This document
        specifies the functional requirements for the physical :term:`OBD-II`
        :term:`diagnostic connector`. The equivalent international standard is
        :term:`ISO 15031-3`.

    Type A diagnostic connector
        A :term:`diagnostic connector` defined in Figure A.1 of
        :term:`ISO 15031-3`.


.. target-notes::

.. _`International Organization for Standardization`: https://www.iso.org/
.. _`SAE International`: https://www.sae.org/
